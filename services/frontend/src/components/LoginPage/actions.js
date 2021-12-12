
export const SET_USER = 'DIARY:SET_USER';

export const TOKEN_COOKIE = 'Authorization';

export const loginAction = (creds, history) => async (dispatch, getRootState) => {
    const resp = await fetch('https://online-diary-mathape.herokuapp.com/api/v1/auth/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ ...creds }),
    });

    const data = await resp.json();
    document.cookie = `${TOKEN_COOKIE}=${data.access_token}`;

    await loadUserProfile(history)(dispatch, getRootState);
};

const getAccessTokenFromCookie = data => {
    const start = data.indexOf(`${TOKEN_COOKIE}=`);
    if (start < 0) {
        return null;
    }
    let end = data.indexOf(';', start);
    if (end < 1) {
        end = undefined;
    }
    return data.substring(start + TOKEN_COOKIE.length + 1, end);
}

export const loadUserProfile = history => async (dispatch, _getRootState) => {
    const cookies = document.cookie;
    const token = getAccessTokenFromCookie(cookies);
    if (!token) {
        history.push('/login');
        return;
    }
    console.log(token);

    const resp = await fetch('https://online-diary-mathape.herokuapp.com/api/v1/users/me', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        },
    });

    const profile = await resp.json();
    console.log(profile);

    dispatch({ type: SET_USER, profile });
};

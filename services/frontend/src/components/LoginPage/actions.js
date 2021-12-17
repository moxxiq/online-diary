
import { TOKEN_COOKIE, getAccessTokenFromCookie, eraseCookie } from '../../helpers/auth'

export const SET_USER = 'DIARY:SET_USER';
export const REMOVE_USER = 'DIARY:REMOVE_USER';
export const SET_WORKPLACE = 'DIARY:SET_WORKPLACE';

export const setCurrentWorkplace = (workplace_id) => async (dispatch, getRootState) => {
    dispatch({ type: SET_WORKPLACE, currentWorkplace: workplace_id });
};


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

export const loadUserProfile = history => async (dispatch, _getRootState) => {
    const token = getAccessTokenFromCookie();
    if (!token) {
        history.push('/login');
        return;
    }

    const resp = await fetch('https://online-diary-mathape.herokuapp.com/api/v1/users/me', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        },
    });

    const profile = await resp.json();

    dispatch({ type: SET_USER, profile });
};


export const logoutAction = (history) => async (dispatch, getRootState) => {
    eraseCookie(TOKEN_COOKIE);
    await removeUserProfile(history)(dispatch, getRootState);
};

export const removeUserProfile = history => async (dispatch, _getRootState) => {
    const token = getAccessTokenFromCookie();
    if (!token) {
        console.log('Logged out, token: ', token);
    }
    dispatch({ type: REMOVE_USER });
};
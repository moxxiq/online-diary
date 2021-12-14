export const TOKEN_COOKIE = 'Authorization';

export const getAccessTokenFromCookie = () => {
    const cookies = document.cookie;
    const start = cookies.indexOf(`${TOKEN_COOKIE}=`);
    if (start < 0) {
        return null;
    }
    let end = cookies.indexOf(';', start);
    if (end < 1) {
        end = undefined;
    }
    return cookies.substring(start + TOKEN_COOKIE.length + 1, end);
}

export const eraseCookie = name => {   
    document.cookie = name+'=; Max-Age=-99999999;';  
}
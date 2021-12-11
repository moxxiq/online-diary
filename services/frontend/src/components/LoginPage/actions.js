import { login } from '../../services/user';

export const SET_USER = 'CHAT_ACTION:SET_USER';

export const loginAction = creds => async (dispatch, getRootState) => {
    const profile = await login(creds);
    dispatch({ type: SET_USER, profile });
};

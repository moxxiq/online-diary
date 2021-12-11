import decodeJwt from 'jwt-decode';
import { BACKEND_URL } from '../config';

export const isAuthenticated = () => {
  const permissions = localStorage.getItem('token_type');
  console.log({permissions})
  if (!permissions) {
    return false;
  }
  return permissions === 'bearer' || permissions === 'admin' ? true : false;
};

/**
 * Login to backend and store JSON web token on success
 *
 * @param email
 * @param password
 * @returns JSON data containing access token on success
 * @throws Error on http errors or failed attempts
 */
export const login = async (email: string, password: string) => {
  // Assert email or password is not empty
  if (!(email.length > 0) || !(password.length > 0)) {
    throw new Error('Email or password was not provided');
  }
  const formData = new FormData();
  // OAuth2 expects form data, not JSON data
  formData.append('username', email);
  formData.append('password', password);

  const request = new Request(`${BACKEND_URL}/auth/token`, {
    method: 'POST',
    body: formData,
  });

  const response = await fetch(request);

  if (response.status === 500) {
    throw new Error('Internal server error');
  }

  const data = await response.json();

  if (response.status > 400 && response.status < 500) {
    if (data.detail) {
      throw data.detail;
    }
    throw data;
  }

  if ('access_token' in data) {
    console.log({data})
    const decodedToken: any = decodeJwt(data['access_token']);
    localStorage.setItem('token', data['access_token']);
    localStorage.setItem('token_type', data['token_type']);
  }

  return data;
};

export const logout = () => {
  localStorage.removeItem('token');
  localStorage.removeItem('token_type');
};

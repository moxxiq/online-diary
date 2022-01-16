
const LOCAL_URL = 'http://localhost:8002';
const GLOBAL_URL = 'https://online-diary-mathape.herokuapp.com';
const IS_LOCAL = window.location.hostname === 'localhost';

export const BASE_URL = IS_LOCAL ? LOCAL_URL : GLOBAL_URL; // with local DB
// export const BASE_URL = !IS_LOCAL ? LOCAL_URL : GLOBAL_URL; // with global server

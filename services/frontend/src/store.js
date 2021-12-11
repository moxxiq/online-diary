import { createStore, applyMiddleware, compose } from 'redux';
import loginReducer from './components/LoginPage/reducer';

import thunk from 'redux-thunk';

const initialState = {};

const middlewares = [ thunk ];
const composedEnhancers = compose(
    applyMiddleware(...middlewares)
);

const store = createStore(
    loginReducer,
    initialState,
    composedEnhancers
);

export default store;
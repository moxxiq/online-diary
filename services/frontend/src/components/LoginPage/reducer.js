import { SET_USER, REMOVE_USER } from './actions';

export default (state = {}, action) => {
    switch (action.type) {
        case SET_USER:
            return {
                ...state,
                profile: action.profile,
            };
        case REMOVE_USER:
            return {
                ...state,
                profile: null
            }
        default:
            return state;
    }
};

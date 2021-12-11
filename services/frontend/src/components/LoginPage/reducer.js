import { SET_USER } from './actions';

export default (state = {}, action) => {
    switch (action.type) {
        case SET_USER:
            return {
                ...state,
                profile: action.profile,
            };
        default:
            return state;
    }
};

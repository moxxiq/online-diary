import { SET_USER, REMOVE_USER, SET_WORKPLACE } from "./actions";

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
        profile: null,
      };
    case SET_WORKPLACE:
      return {
        ...state,
        currentWorkplace: action.currentWorkplace,
      };
    default:
      return state;
  }
};

import { getAccessTokenFromCookie } from "./auth";
import { BASE_URL } from './../config';

export const profile_fullname = (profile, short = false) => {
  if (short) {
    return `${profile.surname} ${profile.name[0]}. ${
      profile.midname && profile.midname[0]
    }.`;
  }
  return `${profile.surname} ${profile.name} ${
    profile.midname && profile.midname
  }`;
};

export const type_to_str = (n) => {
  switch (n) {
    case 1:
      return "Admin";
    case 2:
      return "Teacher";
    case 3:
      return "Student";
    default:
      return "Unknown";
  }
};

export const get_student_workplaces = async (user_id) => {
  const result = await fetch(
    `${BASE_URL}/api/v1/students/${user_id}/workplaces/detailed`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );
  return result.json();
};

export const get_teacher_workplaces = async (user_id) => {
  const result = await fetch(
    `${BASE_URL}/api/v1/teachers/${user_id}/workplaces/detailed`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );
  return result.json();
};

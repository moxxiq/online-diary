import { getAccessTokenFromCookie } from "./auth";

export const get_classname = ({ class_name, class_number }) => {
  const currentTime = new Date();
  const month = currentTime.getMonth() + 1;
  const year = currentTime.getFullYear();

  const number = year - class_number + parseInt(month / 9);

  return `${number}-${class_name}`;
};

export const get_workplace_str = (workplace) => {
  if (workplace.surname) {
    return `${workplace.subject_name} ${workplace.surname} ${workplace.name} ${workplace.midname}`;
  }
  return `${workplace.subject_name} ${get_classname(workplace)}`;
};

export const get_works = async (workplace_id) => {
  const result = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/workplaces/${workplace_id}/works/`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );
  return result.json();
};

export const get_mark = async (work_id, student_id) => {
  const result = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/works/${work_id}/students/${student_id}/marks/`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );
  return result.json();
};

export const get_work_types = async () => {
  const result = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/work_types/`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );
  return result.json();
};

export const get_workplace_student = async (workplace_id) => {
  const result = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/workplace/${workplace_id}/diary/works/`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );
  return result.json();
};

export const get_workplace_teacher = async (workplace_id) => {
  const result = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/workplace/${workplace_id}/journal/works/`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );
  return result.json();
};

export const get_students_from_workplace = async (workplace_id) => {
  let data = await (
    await fetch(
      `https://online-diary-mathape.herokuapp.com/api/v1/workplaces/${workplace_id}/`,
      {
        method: "GET",
        headers: {
          Authorization: `Bearer ${getAccessTokenFromCookie()}`,
        },
      }
    )
  ).json();

  console.log({ data });
  let result = (
    await fetch(
      `https://online-diary-mathape.herokuapp.com/api/v1/classes/${data.class_id}/students/`,
      {
        method: "GET",
        headers: {
          Authorization: `Bearer ${getAccessTokenFromCookie()}`,
        },
      }
    )
  ).json();
  console.log({ result });
  return result;
};

// export const
// get_mark

export const get_mark_str = (mark) => {
  return `${mark.subject_name} ${get_classname(mark)}`;
};

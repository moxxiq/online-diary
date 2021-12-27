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
    `https://online-diary-mathape.herokuapp.com/api/v1/workplaces/${workplace_id}/works`,
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
    `https://online-diary-mathape.herokuapp.com/api/v1/works/${work_id}/students/${student_id}/marks`,
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
    `https://online-diary-mathape.herokuapp.com/api/v1/work_types`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );
  return result.json();
};

export const get_works_student = async (workplace_id) => {
  const result = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/workplace/${workplace_id}/diary/works`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );
  return result.json();
};

export const get_works_teacher = async (workplace_id) => {
  const result = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/workplace/${workplace_id}/journal/works`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );
  return result.json();
};

export const get_workplace = async (workplace_id) => {
  const result = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/workplaces/${workplace_id}`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );
  return result.json();
};

export const get_students_from_class = async (class_id) => {
  const result = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/classes/${class_id}/students`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );
  return result.json();
};

// export const
// get_mark

export const get_mark_str = (mark) => {
  return `${mark.subject_name} ${get_classname(mark)}`;
};

export const getMarkId = async ({ work_id, student_id }) => {
  // Default options are marked with *
  const response = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/works/${work_id}/students/${student_id}/marks`,
    {
      method: "GET", // *GET, POST, PUT, DELETE, etc.
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );

  if (response.status === 404) {
    return -1;
  }

  return (await response.json()).id; // parses JSON response into native JavaScript objects
};

export const createMark = async (data = {}) => {
  // Default options are marked with *
  const response = await fetch(
    "https://online-diary-mathape.herokuapp.com/api/v1/marks",
    {
      method: "POST", // *GET, POST, PUT, DELETE, etc.
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
      body: JSON.stringify(data), // body data type must match "Content-Type" header
    }
  );

  return response.json(); // parses JSON response into native JavaScript objects
};

export const editMark = async ({ id, data }) => {
  // Default options are marked with *
  console.log({ id, data });
  const response = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/marks/${id}`,
    {
      method: "PUT", // *GET, POST, PUT, DELETE, etc.
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
      body: JSON.stringify(data), // body data type must match "Content-Type" header
    }
  );

  return response.json(); // parses JSON response into native JavaScript objects
};

export const createWork = async (data = {}) => {
  // Default options are marked with *
  const response = await fetch(
    "https://online-diary-mathape.herokuapp.com/api/v1/works",
    {
      method: "POST", // *GET, POST, PUT, DELETE, etc.
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
      body: JSON.stringify(data), // body data type must match "Content-Type" header
    }
  );

  return response.json(); // parses JSON response into native JavaScript objects
};

export const editWork = async ({ id, data }) => {
  // Default options are marked with *
  const response = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/works/${id}`,
    {
      method: "PUT", // *GET, POST, PUT, DELETE, etc.
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
      body: JSON.stringify(data), // body data type must match "Content-Type" header
    }
  );

  return response.json(); // parses JSON response into native JavaScript objects
};

export const deleteWork = async (id) => {
  // Default options are marked with *
  const response = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/works/${id}`,
    {
      method: "DELETE", // *GET, POST, PUT, DELETE, etc.
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );

  return response.json(); // parses JSON response into native JavaScript objects
};


export const getWork = async (id) => {
  // Default options are marked with *
  const response = await fetch(
    `https://online-diary-mathape.herokuapp.com/api/v1/works/${id}`,
    {
      method: "GET", // *GET, POST, PUT, DELETE, etc.
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${getAccessTokenFromCookie()}`,
      },
    }
  );

  return response.json(); // parses JSON response into native JavaScript objects
};
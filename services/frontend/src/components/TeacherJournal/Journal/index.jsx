import React, { useEffect, useState } from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { connect } from "react-redux";

import {
  get_works_teacher,
  get_workplace,
  get_students_from_class,
} from "../../../helpers/workplace";
import { profile_fullname } from "../../../helpers/profile";

import { parse_date } from "../../../helpers/other";

function Journal({ profile, currentWorkplace }) {
  const [works, setWorks] = useState([]);
  const [students, setStudents] = useState([]);

  useEffect(() => {
    get_works_teacher(currentWorkplace).then(setWorks);
    get_workplace(currentWorkplace).then((res) => {
      get_students_from_class(res.class_id).then(setStudents);
    });
    // setTimeout(console.log({ works, students }), 3000);
  }, [currentWorkplace]);

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} size="small" aria-label="a dense table">
        <TableHead>
          <TableRow>
            <TableCell colSpan={1}>Студенти</TableCell>
            <TableCell colSpan={works.length} align="center">
              Роботи
            </TableCell>
          </TableRow>
          <TableRow>
            <TableCell colSpan={1}></TableCell>
            {works.map((work) => (
              <TableCell key={work.id} align="right">
                {work.headline}
              </TableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {students.map((student) => (
            <TableRow
              key={student.id}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {profile_fullname(student)}
              </TableCell>
              {works.map((work) => (
                <TableCell align="right">
                  {
                    work.marks?.find((mark) => mark.student_id === student.id)
                      ?.mark || '-'
                  }
                </TableCell>
              ))}
              {/* <TableCell align="right">{row.carbs}</TableCell> */}
              {/* <TableCell align="right">{row.protein}</TableCell> */}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

const mapStateToProps = (rootState) => ({
  profile: rootState?.profile,
  currentWorkplace: rootState?.currentWorkplace,
});

const mapDispatchToProps = {};

export default connect(mapStateToProps, mapDispatchToProps)(Journal);

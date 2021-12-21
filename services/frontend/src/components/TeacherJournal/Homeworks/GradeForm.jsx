import React, { useEffect, useState } from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import InputLabel from "@mui/material/InputLabel";
import OutlinedInput from "@mui/material/OutlinedInput";
import MenuItem from "@mui/material/MenuItem";
import TextField from "@mui/material/TextField";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import { get_students_from_workplace } from "../../../helpers/workplace";

export default function GradeForm({ currentWorkplace, open, setOpen }) {
  //   const [open, setOpen] = React.useState(false);
  const [student, setStudent] = useState(null);
  const [grade, setGrade] = useState(null);
  const [comment, setComment] = useState("");

  const [students, setStudents] = useState([]);

  const handleStudent = (event) => {
    setStudent(Number(event.target.value) || "");
  };

  const handleGrade = (event) => {
    setGrade(Number(event.target.value) || "");
  };

  useEffect(() => {
    get_students_from_workplace(currentWorkplace).then((res) => {
      console.log({ res });
      setStudents(res);
    });
  }, [open, currentWorkplace]);

  const handleClose = (event, reason) => {
    console.log({ students });
    if (reason !== "backdropClick") {
      setOpen(false);
    }
  };

  return (
    <Dialog disableEscapeKeyDown open={open} onClose={handleClose}>
      <DialogTitle>Оцінити роботу</DialogTitle>
      <DialogContent>
        <Box
          component="form"
          sx={{
            display: "flex",
            flexDirection: "column",
            gap: 1,
          }}
        >
          <FormControl sx={{ m: 1, minWidth: 120 }}>
            <InputLabel htmlFor="demo-dialog-native">Студент</InputLabel>
            <Select
              native
              value={student}
              onChange={handleStudent}
              input={<OutlinedInput label="Студент" id="demo-dialog-native" />}
            >
              {students.length
                ? students.map((stud) => (
                    <option
                      key={stud.id}
                      value={stud.id}
                    >{`${stud.surname} ${stud.name}`}</option>
                  ))
                : ""}
            </Select>
          </FormControl>
          <FormControl sx={{ m: 1, minWidth: 120 }}>
            
            <TextField
              id="gradeField"
              value={grade}
              onChange={handleGrade}
              label="Оцінка"
              inputProps={{ inputMode: "numeric", pattern: "[0-9]*" }}
            />
          </FormControl>
          <FormControl sx={{ m: 1, minWidth: 120, alignSelf: "flex-end" }}>
            <TextField fullWidth label="Коментар" id="commentField" />
          </FormControl>
        </Box>
      </DialogContent>
      <DialogActions>
        <Button onClick={handleClose}>Cancel</Button>
        <Button onClick={handleClose}>Ok</Button>
      </DialogActions>
    </Dialog>
  );
}

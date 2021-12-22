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
import {
  get_workplace,
  get_students_from_class,
  createWork
} from "../../../helpers/workplace";

export default function WorkForm({
  currentWorkplace,
  openWork,
  setOpenWork,
  openWorkType,
  work_id_form,
}) {
  const [student_id, setStudent] = useState(null);
  const [mark, setMark] = useState(null);
  const [comment, setComment] = useState("");
  
  const [headline, setHeadline] = useState("Назва роботи");
  const [deadline, setDeadline] = useState(null);
  const [work_type_id, setWorkTypeId] = useState(0);
  const [description, setDescription] = useState("Опис роботи");

  const [students, setStudents] = useState([]);

  const request_data = () => ({
    work_type_id: work_id_form,
    student_id,
    mark,
    comment,
  });

  const handleStudent = (event) => {
    setStudent(Number(event.target.value) || "");
  };

  const handleMark = (event) => {
    setMark(Number(event.target.value) || "");
  };

  const handleComment = (event) => {
    setComment(String(event.target.value) || "");
  };

  useEffect(() => {
    get_workplace(currentWorkplace).then((res) => {
      get_students_from_class(res.class_id).then(setStudents);
    });
  }, [openWork, currentWorkplace]);

  const handleClose = (event, reason) => {
    console.log({ student_id, mark, comment, students });

    if (reason === "submit") {
      // postData(request_data()).then((res) => console.log(res));
      // request_data
    }

    if (reason !== "backdropClick") {
      setOpenWork(false);
    }
  };

  return (
    <Dialog disableEscapeKeyDown open={openWork} onClose={handleClose}>
      <DialogTitle>Створити роботу</DialogTitle>
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
            <Select value={student_id || ""} onChange={handleStudent}>
              {students.length ? (
                students.map((stud) => (
                  <MenuItem
                    key={stud.id}
                    value={stud.id}
                  >{`${stud.surname} ${stud.name}`}</MenuItem>
                ))
              ) : (
                <></>
              )}
            </Select>
          </FormControl>
          <FormControl sx={{ m: 1, minWidth: 120 }}>
            <TextField
              type="text"
              id="gradeField"
              value={mark || ""}
              onChange={handleMark}
              label="Оцінка"
              inputProps={{ inputMode: "numeric", pattern: "[0-9]*" }}
            />
          </FormControl>
          <FormControl sx={{ m: 1, minWidth: 120, alignSelf: "flex-end" }}>
            <TextField
              id="commentField"
              onChange={handleComment}
              value={comment || ""}
              fullWidth
              label="Коментар"
              inputProps={{inputMode: "text", maxLength: 50}}
            />
          </FormControl>
        </Box>
      </DialogContent>
      <DialogActions>
        <Button onClick={handleClose}>Відмінити</Button>
        <Button onClick={(e) => handleClose(e, "submit")}>Виставити</Button>
      </DialogActions>
    </Dialog>
  );
}

import React, { useEffect, useState } from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import InputLabel from "@mui/material/InputLabel";
import AdapterDateFns from "@mui/lab/AdapterDateFns";
import LocalizationProvider from "@mui/lab/LocalizationProvider";
import DateTimePicker from "@mui/lab/DateTimePicker";
import MenuItem from "@mui/material/MenuItem";
import TextField from "@mui/material/TextField";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import {
  get_work_types,
  createWork,
  editWork,
  deleteWork,
  getWork,
} from "../../../helpers/workplace";

export default function WorkForm({
  currentWorkplace,
  openWork,
  setOpenWork,
  openWorkType,
  work_id_form,
  handleOpenToast,
}) {
  //   const [open, setOpen] = React.useState(false);
  const [work_types, setWorkTypes] = useState([]);
  const [work_type_id, setWorkTypeId] = useState(1);
  const [headline, setHeadline] = useState("Назва роботи");
  const [deadline, setDeadline] = useState(new Date());
  const [description, setDescription] = useState("Опис роботи");

  const request_data = () => ({
    headline,
    deadline,
    description,
    work_type_id,
    workplace_id: currentWorkplace,
  });

  const handleWorkType = (event) => {
    setWorkTypeId(Number(event.target.value) || "");
  };

  const handleDeadline = (event) => {
    setDeadline(Date(event.target.value) || "");
  };

  const handleHeadline = (event) => {
    setHeadline(String(event.target.value) || "");
  };

  const handleDescription = (event) => {
    setDescription(String(event.target.value) || "");
  };

  useEffect(() => {
    get_work_types().then(setWorkTypes);
  }, [openWork, currentWorkplace]);

  useEffect(() => {
    openWorkType === "EDIT" &&
      getWork(work_id_form).then((work_data) => {
        work_data.headline && setHeadline(work_data.headline);
        work_data.deadline && setDeadline(work_data.deadline);
        work_data.description && setDescription(work_data.description);
        work_data.work_type_id && setWorkTypeId(work_data.work_type_id);
      });
  }, [work_id_form]);

  const handleClose = (event, reason, edit) => {
    // console.log({ work_types, openWorkType, work_id_form, ...request_data() });

    if (reason === "submit") {
      switch (openWorkType) {
        case "CREATE":
          createWork(request_data())
            .then((res) => {
              console.log(res);
              handleOpenToast("WORK_OK");
            })
            .catch((err) => {
              console.log({ err });
              handleOpenToast("ERROR");
            });
          break;
        case "EDIT":
          editWork({ id: work_id_form, data: request_data() })
            .then((res) => {
              console.log(res);
              handleOpenToast("WORK_EDIT");
            })
            .catch((err) => {
              console.log({ err });
              handleOpenToast("ERROR");
            });
          break;
        case "DELETE":
          deleteWork(work_id_form)
            .then((res) => {
              console.log(res);
              handleOpenToast("WORK_DELETE");
            })
            .catch((err) => {
              console.log({ err });
              handleOpenToast("ERROR");
            });
          break;
      }

      setOpenWork(false);
    }

    if (reason !== "backdropClick") {
      setOpenWork(false);
      handleOpenToast("CLOSE_FORM");
    }
  };

  return (
    <Dialog disableEscapeKeyDown open={openWork} onClose={handleClose}>
      <DialogTitle>
        {(openWorkType === "EDIT" && "Змінити опис") ||
          (openWorkType === "CREATE" && "Створити роботу") ||
          (openWorkType === "DELETE" && "Видалити роботу")}
      </DialogTitle>
      <DialogContent>
        {openWorkType !== "DELETE" && (
          <Box
            component="form"
            sx={{
              display: "flex",
              flexDirection: "column",
              gap: 1,
            }}
          >
            <FormControl sx={{ m: 1, minWidth: 120 }}>
              <InputLabel htmlFor="demo-dialog-native">Тип роботи</InputLabel>
              <Select value={work_type_id} onChange={handleWorkType}>
                {work_types.length ? (
                  work_types.map((w_type) => (
                    <MenuItem
                      key={w_type.id}
                      value={w_type.id}
                    >{`${w_type.name}`}</MenuItem>
                  ))
                ) : (
                  <></>
                )}
              </Select>
            </FormControl>
            <FormControl sx={{ m: 1, minWidth: 120 }}>
              <LocalizationProvider dateAdapter={AdapterDateFns}>
                <DateTimePicker
                  renderInput={(props) => <TextField {...props} />}
                  label="Дедлайн"
                  disablePast
                  maxDate={
                    new Date().getMonth() > 5
                      ? new Date(new Date().getFullYear(), 11, 30, 23)
                      : new Date(new Date().getFullYear(), 5, 15, 23)
                  }
                  value={deadline}
                  onChange={(newValue) => {
                    setDeadline(newValue);
                  }}
                />
              </LocalizationProvider>
            </FormControl>
            <FormControl sx={{ m: 1, minWidth: 120, alignSelf: "flex-end" }}>
              <TextField
                id="headlineField"
                onChange={handleHeadline}
                value={headline}
                fullWidth
                label="Назва роботи"
                inputProps={{ inputMode: "text", maxLength: 30 }}
              />
            </FormControl>
            <FormControl sx={{ m: 1, minWidth: 120, alignSelf: "flex-end" }}>
              <TextField
                id="descriptionField"
                onChange={handleDescription}
                value={description}
                fullWidth
                label="Опис роботи"
                inputProps={{ inputMode: "text", maxLength: 80 }}
              />
            </FormControl>
          </Box>
        )}
      </DialogContent>
      <DialogActions>
        <Button onClick={handleClose}>Відмінити</Button>
        {openWorkType !== "DELETE" ? (
          <Button
            sx={{ color: "green" }}
            onClick={(e) => handleClose(e, "submit")}
          >
            Зберегти
          </Button>
        ) : (
          <Button
            sx={{ color: "red" }}
            onClick={(e) => handleClose(e, "submit")}
          >
            Видалити
          </Button>
        )}
      </DialogActions>
    </Dialog>
  );
}

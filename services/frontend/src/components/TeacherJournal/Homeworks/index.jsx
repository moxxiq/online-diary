import React, { useState, useEffect } from "react";
import Button from "@mui/material/Button";
import Accordion from "@mui/material/Accordion";
import AccordionDetails from "@mui/material/AccordionDetails";
import AccordionSummary from "@mui/material/AccordionSummary";
import Typography from "@mui/material/Typography";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import Avatar from "@mui/material/Avatar";
import Snackbar from "@mui/material/Snackbar";
import MuiAlert from "@mui/material/Alert";
import SportsScoreIcon from "@mui/icons-material/SportsScore";
import BorderAllIcon from "@mui/icons-material/BorderAll";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import { connect } from "react-redux";

import GradeForm from "./GradeForm";
import WorkForm from "./WorkForm";

import { get_works_teacher, get_work_types } from "../../../helpers/workplace";
import { parse_date } from "../../../helpers/other";

const Alert = React.forwardRef(function Alert(props, ref) {
  return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

function Homeworks({ profile, currentWorkplace }) {
  const [expanded, setExpanded] = useState(false);
  const [works, setWorks] = useState([]);
  const [work_types, setWorkTypes] = useState({});
  const [open, setOpen] = useState(false);
  const [openWork, setOpenWork] = useState(false);
  const [openToast, setOpenToast] = useState(false);
  const [toastSeverity, setToastSeverity] = useState("success");
  const [toastMessage, setToastMessage] = useState("success");

  const [openWorkType, setOpenWorkType] = useState(""); // "CREATE", "EDIT", "DELETE"

  const [work_id_form, setWorkIdForm] = useState(null);

  useEffect(() => {
    get_work_types().then((res_arr) => {
      let result_types = {};
      function setPlace(work_type) {
        result_types[work_type.id] = work_type.name;
      }
      res_arr.forEach(setPlace);
      setWorkTypes(result_types);
    });
    get_works_teacher(currentWorkplace).then(setWorks);
    setTimeout(console.log({ works, work_types }), 3000);
  }, [currentWorkplace, openWork]);

  const handleChange = (panel) => (event, isExpanded) => {
    setExpanded(isExpanded ? panel : false);
    setTimeout(console.log({ works, work_types }), 1000);
  };

  const handleClickOpen = (work_id) => {
    setWorkIdForm(work_id);
    setOpen(true);
  };

  const handleClickOpenWork = (open_type, work_id = null) => {
    setOpenWorkType(open_type);
    work_id && setWorkIdForm(work_id);
    setOpenWork(true);
  };

  const handleOpenToast = (reason) => {
    switch (reason) {
      case "MARK_OK":
        setToastSeverity("success");
        setToastMessage("Оцінка виставлена успішно!");
        break;
      case "WORK_OK":
        setToastSeverity("success");
        setToastMessage("Робота створена успішно!");
        break;
      case "ERROR":
        setToastSeverity("error");
        setToastMessage("Помилка запиту!");
        break;
      case "CLOSE_FORM":
        setToastSeverity("info");
        setToastMessage("Ви відмінили зміни у формі");
        break;
    }
    setOpenToast(true);
  };

  const handleCloseToast = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }

    setOpenToast(false);
  };

  return (
    <div>
      {Array.isArray(works) ? (
        works.map((work) => (
          <Accordion
            expanded={expanded === work.id}
            onChange={handleChange(work.id)}
            key={work.id}
          >
            <AccordionSummary
              expandIcon={<ExpandMoreIcon />}
              aria-controls={`panel${work.id}bh-content`}
              id={`panel${work.id}bh-header`}
            >
              <Typography sx={{ width: "33%", flexShrink: 0 }}>
                {work.headline}
              </Typography>
              <Typography sx={{ color: "text.secondary", ml: "250px" }}>
                {`Дедлайн: ${parse_date(work.deadline)}`}
              </Typography>
            </AccordionSummary>
            <AccordionDetails>
              <List
                sx={{
                  width: "100%",
                  maxWidth: 360,
                  bgcolor: "background.paper",
                }}
              >
                <ListItem>
                  <ListItemAvatar>
                    <Avatar>
                      <BorderAllIcon />
                    </Avatar>
                  </ListItemAvatar>
                  <ListItemText
                    primary={work_types[work.work_type_id]}
                    secondary={`Опис: ${work.description}`}
                  />
                </ListItem>
                <ListItem>
                  <ListItemAvatar>
                    <Avatar>
                      <SportsScoreIcon />
                    </Avatar>
                  </ListItemAvatar>
                  <ListItemText
                    primary="Створено -- Дедлайн"
                    secondary={`${parse_date(
                      work.creation_date
                    )} -- ${parse_date(work.deadline)}`}
                  />
                </ListItem>
                <ListItem>
                  <Button
                    variant="text"
                    onClick={() => handleClickOpen(work.id)}
                  >
                    Виставити оцінку
                  </Button>
                </ListItem>
              </List>
            </AccordionDetails>
          </Accordion>
        ))
      ) : (
        <>{typeof works}</>
      )}
      <GradeForm
        {...{ currentWorkplace, open, setOpen, work_id_form, handleOpenToast }}
      />
      <WorkForm
        {...{
          currentWorkplace,
          openWork,
          setOpenWork,
          openWorkType,
          work_id_form,
          handleOpenToast,
        }}
      />

      <Button
        sx={{ ml: "40%", mt: 1, color: "green" }}
        onClick={() => handleClickOpenWork("CREATE", null)}
      >
        Створити нову роботу
      </Button>
      <Snackbar
        open={openToast}
        autoHideDuration={5000}
        onClose={handleCloseToast}
      >
        <Alert
          onClose={handleCloseToast}
          severity={toastSeverity}
          sx={{ width: "100%" }}
        >
          {toastMessage}
        </Alert>
      </Snackbar>
    </div>
  );
}

// secondary={`Оцінки: ${work.marks[0].comment}`}
// primary={parse_date(work.marks[0].creation_date)}
// secondary={`Оцінки: ${work.marks[0].comment}`}
// work.marks.length ? "" : ""}

const mapStateToProps = (rootState) => ({
  profile: rootState?.profile,
  currentWorkplace: rootState?.currentWorkplace,
});

const mapDispatchToProps = {};

export default connect(mapStateToProps, mapDispatchToProps)(Homeworks);

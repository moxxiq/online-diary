import * as React from "react";
import Accordion from "@mui/material/Accordion";
import AccordionDetails from "@mui/material/AccordionDetails";
import AccordionSummary from "@mui/material/AccordionSummary";
import Typography from "@mui/material/Typography";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import Avatar from "@mui/material/Avatar";
import DateRangeIcon from "@mui/icons-material/DateRange";
import SportsScoreIcon from "@mui/icons-material/SportsScore";
import GradeIcon from "@mui/icons-material/Grade";
import BorderAllIcon from "@mui/icons-material/BorderAll";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import { get_workplace_student, get_work_types } from "../../helpers/workplace";
import { parse_date } from "../../helpers/other";
import { connect } from "react-redux";

function StudentSubject({ profile, currentWorkplace }) {
  const [expanded, setExpanded] = React.useState(false);
  const [works, setWorks] = React.useState([]);
  const [work_types, setWorkTypes] = React.useState({});
  React.useEffect(() => {
    get_work_types().then((res_arr) => {
      let result_types = {};
      function setPlace(work_type) {
        result_types[work_type.id] = work_type.str;
      }
      res_arr.forEach(setPlace);
      setWorkTypes(result_types);
    });
    get_workplace_student(currentWorkplace).then(setWorks);
    console.log({ works, work_types });
  }, [currentWorkplace]);

  const handleChange = (panel) => (event, isExpanded) => {
    setExpanded(isExpanded ? panel : false);
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
              <Typography sx={{ color: "text.secondary" }}>
                {work.description}
              </Typography>
              <Typography sx={{ color: "text.secondary", ml: "150px" }}>
                {work.marks.length
                  ? `Оцінка: ${work.marks[0].mark}`
                  : "Не виставлено"}
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
                    primary="Вид роботи"
                    secondary={work_types[work.work_type_id]}
                  />
                </ListItem>
                <ListItem>
                  <ListItemAvatar>
                    <Avatar>
                      <SportsScoreIcon />
                    </Avatar>
                  </ListItemAvatar>
                  <ListItemText
                    primary="Початок -- Дедлайн"
                    secondary={`${parse_date(
                      work.creation_date
                    )} -- ${parse_date(work.deadline)}`}
                  />
                </ListItem>
                {work.marks.length ? (
                  <ListItem>
                    <ListItemAvatar>
                      <Avatar>
                        <GradeIcon />
                      </Avatar>
                    </ListItemAvatar>
                    <ListItemText
                      primary={parse_date(work.marks[0].creation_date)}
                      secondary={`Коментар: ${work.marks[0].comment}`}
                    />
                  </ListItem>
                ) : (
                  ""
                )}
              </List>
            </AccordionDetails>
          </Accordion>
        ))
      ) : (
        <>{typeof works}</>
      )}
    </div>
  );
}

const mapStateToProps = (rootState) => ({
  profile: rootState?.profile,
  currentWorkplace: rootState?.currentWorkplace,
});

const mapDispatchToProps = {};

export default connect(mapStateToProps, mapDispatchToProps)(StudentSubject);

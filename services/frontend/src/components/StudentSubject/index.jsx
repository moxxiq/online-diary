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
import { get_works_student, get_work_types } from "../../helpers/workplace";
import { parse_date } from "../../helpers/other";
import { connect } from "react-redux";
import { Container, Box } from "@mui/material";
import { styled } from "@mui/material/styles";

const MarkDiv = styled("div")(({ theme }) => ({
  ...theme.typography.button,
  backgroundColor: theme.palette.background.paper,
  padding: theme.spacing(1),
}));

function StudentSubject({ profile, currentWorkplace }) {
  const [expanded, setExpanded] = React.useState(false);
  const [works, setWorks] = React.useState([]);
  const [work_types, setWorkTypes] = React.useState({});
  React.useEffect(() => {
    get_work_types().then((res_arr) => {
      let result_types = {};
      function setPlace(work_type) {
        result_types[work_type.id] = work_type.name;
      }
      res_arr.forEach(setPlace);
      setWorkTypes(result_types);
    });
    get_works_student(currentWorkplace).then(setWorks);
    console.log({ works, work_types });
  }, [currentWorkplace]);

  const handleChange = (panel) => (event, isExpanded) => {
    setExpanded(isExpanded ? panel : false);
  };

  return (
    <Container>
      {Array.isArray(works) ? (
        works.map((work) => (
          <Box key={work.id} sx={{ display: "flex", p: 1, width: "lg" }}>
            <Accordion
              sx={{ flex: 1.6 }}
              expanded={expanded === work.id}
              onChange={handleChange(work.id)}
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
                      primary="Створено -- Дедлайн"
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
            <Box sx={{ m: 2, flex: 0.2, minWidth: "200px" }}>
              <Typography sx={{ color: "text.secondary" }}>
                {work.marks.length
                  ? `Оцінка: ${work.marks[0].mark}`
                  : "Не виставлено"}
              </Typography>
            </Box>
          </Box>
        ))
      ) : (
        <>{typeof works}</>
      )}

      <MarkDiv>
        {`Ваша загальна оцінка становить: ${
          works.length
            ? works.reduce((result, w) => result + (w.marks.length ? w.marks[0].mark : 0), 0)
            : 0
        }`}
      </MarkDiv>
    </Container>
  );
}

const mapStateToProps = (rootState) => ({
  profile: rootState?.profile,
  currentWorkplace: rootState?.currentWorkplace,
});

const mapDispatchToProps = {};

export default connect(mapStateToProps, mapDispatchToProps)(StudentSubject);

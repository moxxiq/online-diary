import React, { useEffect } from "react";
import { useHistory } from "react-router-dom";
import { styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import IconButton from "@mui/material/IconButton";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import SchoolIcon from "@mui/icons-material/School";
import {
  get_teacher_workplaces,
  profile_fullname,
} from "../../helpers/profile";
import { get_classname } from "../../helpers/workplace";
import { setCurrentWorkplace } from "../../components/LoginPage/actions";
import { connect } from "react-redux";

const Demo = styled("div")(({ theme }) => ({
  backgroundColor: theme.palette.background.paper,
}));

function ClassesList({ profile, currentWorkplace, setCurrentWorkplace }) {
  const history = useHistory();
  const [dense, setDense] = React.useState(false);
  const [secondary, setSecondary] = React.useState(false);
  const [workplaces, setWorkplaces] = React.useState(null);

  useEffect(() => {
    get_teacher_workplaces(profile?.id).then((w) => {
      setWorkplaces(w);
    });
  }, [profile]);

  useEffect(() => {
    console.log({ workplaces });
  }, [workplaces]);

  const handleClickItem = (workplace) => {
    if (workplace && workplace > 0) {
      setCurrentWorkplace(workplace);
      history.push("/dashboard");
    }
  };

  return (
    <Box sx={{ flexGrow: 1, mr: 2 }}>
      <Typography sx={{ mt: 4, mb: 2 }} variant="h6" component="div">
        Класи, де ви викладаєте
      </Typography>
      <Demo>
        <List dense={dense}>
          {Array.isArray(workplaces) ? (
            workplaces.map((workplace) => (
              <ListItem
                key={workplace.id}
                onClick={() => handleClickItem(workplace.id)}
              >
                <ListItemIcon>
                  <SchoolIcon />
                </ListItemIcon>
                <ListItemText
                  primary={`${get_classname(workplace)}`}
                  secondary={`${workplace.subject_name}`}
                />
              </ListItem>
            ))
          ) : (
            <>{typeof workplaces}</>
          )}
        </List>
      </Demo>
    </Box>
  );
}

const mapStateToProps = (rootState) => ({
  profile: rootState?.profile,
  currentWorkplace: rootState?.currentWorkplace,
});

const mapDispatchToProps = {
  setCurrentWorkplace,
};

export default connect(mapStateToProps, mapDispatchToProps)(ClassesList);

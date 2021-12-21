import React, { useEffect } from "react";
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
import { get_teacher_workplaces, profile_fullname } from "../../helpers/profile";
import { get_classname } from "../../helpers/workplace";

const Demo = styled("div")(({ theme }) => ({
  backgroundColor: theme.palette.background.paper,
}));

export default function ClassesList(props) {
  const [dense, setDense] = React.useState(false);
  const [secondary, setSecondary] = React.useState(false);
  const [workplaces, setWorkplaces] = React.useState(null);
  useEffect(() => {
    get_teacher_workplaces(props.profile?.id).then(w => {
      setWorkplaces(w);
    })
  }, [props.profile]);
  useEffect(() => {
    
    console.log({ workplaces });
  }, [workplaces]);
  return (
    <Box sx={{ flexGrow: 1, mr: 2 }}>
      <Typography sx={{ mt: 4, mb: 2 }} variant="h6" component="div">
        Класи, де ви викладаєте
      </Typography>
      <Demo>
        <List dense={dense}>
          {Array.isArray(workplaces)? workplaces.map((workplace) => 
            <ListItem key={workplace.id}>
              <ListItemIcon>
                <SchoolIcon />
              </ListItemIcon>
              <ListItemText
                primary={`${get_classname(workplace)}`}
                secondary={`${workplace.subject_name}`}
              />
            </ListItem>
          ) : <>{typeof(workplaces)}</>}
        </List>
      </Demo>
    </Box>
  );
}

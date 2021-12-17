import React, { useEffect, useState } from "react";
import TextField from "@mui/material/TextField";
import Autocomplete from "@mui/material/Autocomplete";
import Container from "@mui/material/Container";
import Box from "@mui/material/Box";
import parse from "autosuggest-highlight/parse";
import match from "autosuggest-highlight/match";
import { connect } from "react-redux";

import { setCurrentWorkplace } from "../../components/LoginPage/actions";

import StudentSubject from "../../components/StudentSubject";
import TeacherJournal from "../../components/TeacherJournal";

import {
  get_student_workplaces,
  get_teacher_workplaces,
} from "../../helpers/profile";

import { get_workplace_str } from "../../helpers/workplace";

const DashboardPage = ({ profile, currentWorkplace }) => {
  const [workplaces, setWorkplaces] = useState([]);

  useEffect(() => {
    // console.log({
    //   w1: get_student_workplaces(profile),
    //   w2: get_teacher_workplaces(profile),
    // });
    console.log({ profile });
    switch (profile?.type) {
      case 2:
        get_teacher_workplaces(profile.id).then((result) => {
          console.log(result);
          setWorkplaces(result);
        });
        break;
      case 3:
        get_student_workplaces(profile.id).then((result) => {
          console.log(result);
          setWorkplaces(result);
        });
        break;
    }
    console.log({ workplaces });
  }, [profile]);

  return (
    <Container maxWidth="sl">
      <Box
        display="flex"
        flexDirection="column"
        alignItems="center"
        justifyContent="center"
        sx={{ mt: 1, mb: 1 }}
      >
        <Autocomplete
          id="highlights-demo"
          sx={{ width: 300 }}
          options={workplaces}
          getOptionLabel={(option) => get_workplace_str(option)}
          renderInput={(params) => (
            <TextField {...params} label="Highlights" margin="normal" />
          )}
          renderOption={(props, option, { inputValue }) => {
            const matches = match(get_workplace_str(option), inputValue);
            const parts = parse(get_workplace_str(option), matches);

            return (
              <li {...props}>
                <div>
                  {parts.map((part, index) => (
                    <span
                      key={`${option.id}-${index}`}
                      style={{
                        fontWeight: part.highlight ? 700 : 400,
                      }}
                    >
                      {part.text}
                    </span>
                  ))}
                </div>
              </li>
            );
          }}
        />
      </Box>
      {profile?.type === 2 ? <TeacherJournal /> : <StudentSubject />}
    </Container>
  );
};

// Top 100 films as rated by IMDb users. http://www.imdb.com/chart/top
// const top100Films = [
//   { title: 'The Shawshank Redemption', year: 1994 },

const mapStateToProps = (rootState) => ({
  profile: rootState?.profile,
  currentWorkplace: rootState?.currentWorkplace,
});

const mapDispatchToProps = {};

export default connect(mapStateToProps, mapDispatchToProps)(DashboardPage);

import * as React from "react";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";

import Container from "@mui/material/Container";

import ProfileCard from "./ProfileCard";
import SubjectsList from "./SubjectsList";
import ClassesList from "./ClassesList";

import { connect } from "react-redux";

function ProfilePage({ profile }) {
  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="md">
        {/* <Box sx={{ bgcolor: "#cfe8fc", height: "100vh" }}> */}
        <Grid container spacing={2} sx={{ bgcolor: "#cfe8fc" }}>
          <Grid item xs={4}>
            <ProfileCard profile={profile} />
          </Grid>
          <Grid item xs={8}>
            {profile?.type === 2 ? (
              <ClassesList profile={profile} />
            ) : (
              <SubjectsList profile={profile} />
            )}
          </Grid>
        </Grid>
      </Container>
    </React.Fragment>
  );
}

const mapStateToProps = (rootState) => ({
  profile: rootState?.profile,
});

const mapDispatchToProps = {};

export default connect(mapStateToProps, mapDispatchToProps)(ProfilePage);

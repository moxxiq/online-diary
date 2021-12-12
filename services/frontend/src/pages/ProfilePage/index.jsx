import * as React from "react";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";

import Container from "@mui/material/Container";

import ProfileCard from "./ProfileCard";
import InteractiveList from "./SubjectsList";

export default function ProfilePage() {
  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="md">
        {/* <Box sx={{ bgcolor: "#cfe8fc", height: "100vh" }}> */}
        <Grid container spacing={2} sx={{bgcolor: "#cfe8fc"}}>
          <Grid item xs={4}>
            <ProfileCard />
          </Grid>
          <Grid item xs={8}>
            <InteractiveList />
          </Grid>
        </Grid>
      </Container>
    </React.Fragment>
  );
}

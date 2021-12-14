import * as React from "react";
import ButtonGroup from "@mui/material/ButtonGroup";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";

export default function TeacherJournal() {
  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="sl">
        <Box
          display="flex"
          flexDirection="column"
          alignItems="center"
          justifyContent="center"
          sx={{ mt: 1, mb: 1 }}
        >
          <ButtonGroup disableElevation variant="contained">
            <Button>One</Button>
            <Button>Two</Button>
          </ButtonGroup>
        </Box>
        <Container maxWidth="sl">
          <Box sx={{ bgcolor: "#cfe8fc", height: "100vh" }} />
        </Container>
      </Container>
    </React.Fragment>
  );
}

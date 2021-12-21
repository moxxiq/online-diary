import React, { useState, useEffect } from "react";
import ButtonGroup from "@mui/material/ButtonGroup";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Homeworks from "./Homeworks";
import Journal from "./Journal";

export default function TeacherJournal() {
  const [oneOpened, setOneOpened] = useState(true);

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
            <Button
              variant={!oneOpened ? "outlined" : "contained"}
              onClick={() => setOneOpened(true)}
            >
              Роботи
            </Button>
            <Button
              variant={oneOpened ? "outlined" : "contained"}
              onClick={() => setOneOpened(false)}
            >
              Журнал
            </Button>
          </ButtonGroup>
        </Box>
        <Container maxWidth="sl">
          {oneOpened ? <Homeworks /> : <Journal />}
        </Container>
      </Container>
    </React.Fragment>
  );
}

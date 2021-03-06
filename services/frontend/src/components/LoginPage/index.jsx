import React, { useState } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import { TextField, Button, FormLabel } from "@mui/material";
import { loginAction } from "./actions";

import "./style.css";

const LoginPage = ({ profile, loginAction }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [incorrect, setIncorrect] = useState(false);

  const handleLogin = () => {
    loginAction({
      username,
      password,
    }).then((logged) => {
      if (!logged) {
        setIncorrect(true);
      } else {
        setIncorrect(false);
      }
    });

    console.log({ incorrect });
  };

  return (
    <div className="login_page">
      {profile ? (
        <Redirect to={{ path: "/" }} />
      ) : (
        <form
          onSubmit={(event) => {
            event.preventDefault();
            handleLogin();
          }}
          className="login_form"
        >
          <FormLabel>
            Hmmm, I see you haven't logged in to your account so far :({" "}
          </FormLabel>
          <FormLabel>Username</FormLabel>
          <TextField
            className="login_form_item"
            id="filled-basic"
            label="Filled"
            variant="filled"
            type="text"
            onChange={(event) => setUsername(event.target.value)}
          />
          <FormLabel>Password</FormLabel>
          <TextField
            className="login_form_item"
            id="filled-basic"
            label="Filled"
            variant="filled"
            type="password"
            onChange={(event) => setPassword(event.target.value)}
          />
          {incorrect ? (
            <FormLabel sx={{ color: "red" }}>
              Wrong passwrod or email, please try again
            </FormLabel>
          ) : (
            ""
          )}
          <Button
            className="login_form_item"
            variant="contained"
            type="button"
            onClick={handleLogin}
          >
            Continue
          </Button>
        </form>
      )}
    </div>
  );
};

const mapStateToProps = (rootState) => ({
  profile: rootState?.profile,
});

const mapDispatchToProps = {
  loginAction,
};

export default connect(mapStateToProps, mapDispatchToProps)(LoginPage);

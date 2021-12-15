import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import LoginPage from "../../components/LoginPage";
import ProfilePage from "../../pages/ProfilePage";
import DashboardPage from "../../pages/DashboardPage";
import PrivateRoute from "../PrivateRoute";

const Routing = () => {

  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <PrivateRoute Component={ProfilePage} exact path="/" />
        </Route>
        <Route path="/login">
          <LoginPage/>
        </Route>
        <Route path="/dashboard">
          <PrivateRoute exact Component={DashboardPage} path="/dashboard"/>
        </Route>
      </Switch>
    </Router>
  );
};

export default Routing;

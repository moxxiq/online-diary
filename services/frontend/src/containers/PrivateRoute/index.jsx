import React, { useEffect } from "react";
import { loadUserProfile } from "../../components/LoginPage/actions";
import { connect } from "react-redux";
import { Route, Redirect, useHistory } from "react-router-dom";
// import Header from '../../components/Header';
import ResponsiveAppBar from "../../components/ResponsiveAppBar";
import LoginPage from "../../components/LoginPage";

const PrivateRoute = ({ Component, profile, loadUserProfile, ...rest }) => {
  const history = useHistory();
  //   const profile = useSelector(state => state.counter)
  useEffect(() => {
    if (!profile) {
      loadUserProfile(history);
    }
  }, [profile]);
  // d5e42731c79c
  return (
    <Route
      {...rest}
      render={(props) => (
        <>
          {/* <Header /> */}
          <ResponsiveAppBar />
          <Component />
        </>
      )}
    />
  );
};

const mapStateToProps = (rootState) => ({
  profile: rootState?.profile,
});

const mapDispatchToProps = {
  loadUserProfile,
};

export default connect(mapStateToProps, mapDispatchToProps)(PrivateRoute);

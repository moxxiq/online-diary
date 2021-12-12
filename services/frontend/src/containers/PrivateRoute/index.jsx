import React, { useEffect } from 'react';
import { loadUserProfile } from "../../components/LoginPage/actions";
import { connect } from "react-redux";
import { Route, useHistory } from "react-router-dom";
import Header from '../../components/Header';

const PrivateRoute = ({ Component, profile, loadUserProfile, ...rest }) => {
    const history = useHistory();

    useEffect(() => {
        if (!profile) {
            loadUserProfile(history);
        }
    });

    return (<Route {...rest} render={
        (props) => (
            <>
                <Header />
                <Component />
            </>
        )}
    />);
}


const mapStateToProps = rootState => ({
    profile: rootState?.profile
});

const mapDispatchToProps = {
    loadUserProfile
};

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(PrivateRoute);

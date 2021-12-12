import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from 'react-router-dom';
import LoginPage from '../../components/LoginPage';
import ProfilePage from '../../pages/ProfilePage'

const Routing = () => {
    return (
        <Router>
            <Switch>
                <Route exact path="/">
                    <ProfilePage>

                    </ProfilePage>
                </Route>
                <Route path="/login">
                    <LoginPage />
                </Route>
                <Route path="/journal">
                    <LoginPage />
                </Route>
            </Switch>
        </Router>
    );
};

export default Routing;

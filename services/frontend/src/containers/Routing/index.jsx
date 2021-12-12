import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from 'react-router-dom';
import LoginPage from '../../components/LoginPage';

const Routing = () => {
    return (
        <Router>
            <Switch>
                <Route exact path="/">
                    <PrivateRoute Component={MyComponent} exact path="/" />
                </Route>
                <Route path="/login">
                    <LoginPage />
                </Route>
            </Switch>
        </Router>
    );
};

export default Routing;

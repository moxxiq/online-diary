import React  from 'react';
import { connect } from "react-redux";

import './style.css';

const Header = ({ profile }) => {
    return (
        <div className="header">
            <div className="app_name">
                <img src="https://img.icons8.com/cotton/64/000000/chat.png" alt=""/>
                <span>Online Diary</span>
            </div>
            <div className="user_panel">
                <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                     width="24" height="24"
                     viewBox="0 0 172 172"
                     style={{"fill": "#000000"}}>
                    <g fill="none" fillRule="nonzero" stroke="none" strokeWidth="1" strokeLinecap="butt" strokeLinejoin="miter" strokeMiterlimit="10" strokeDasharray="" strokeDashoffset="0" fontFamily="none" fontWeight="none" fontSize="none" textAnchor="none" style={{"mixBlendMode": "normal"}}>
                        <path d="M0,172v-172h172v172z" fill="none" />
                        <g className="notification_logo" fill="#c7ced1">
                            <path d="M86,14.33333c-5.934,0 -10.75,4.816 -10.75,10.75v4.98307c-18.53885,4.77861 -32.25,21.56799 -32.25,41.60026v43l-11.00195,8.28646h-0.014c-2.06676,1.31602 -3.31796,3.59669 -3.31738,6.04688c0,3.95804 3.20863,7.16667 7.16667,7.16667h50.16667h50.16667c3.95804,0 7.16667,-3.20863 7.16667,-7.16667c0.00058,-2.45018 -1.25062,-4.73086 -3.31739,-6.04687l-11.01595,-8.28646v-43c0,-20.03227 -13.71115,-36.82165 -32.25,-41.60026v-4.98307c0,-5.934 -4.816,-10.75 -10.75,-10.75zM71.66667,143.33333c0,7.88333 6.45,14.33333 14.33333,14.33333c7.88333,0 14.33333,-6.45 14.33333,-14.33333z" />
                        </g>
                    </g>
                </svg>
                <div className="user_profile">
                    <img src="https://img.icons8.com/dusk/64/000000/naruto.png" alt=""/>
                    <span>{`${profile?.name || ''} ${profile?.midname || ''} ${profile?.surname || ''}`}</span>
                </div>
            </div>
        </div>
    );
}

const mapStateToProps = rootState => ({
    profile: rootState?.profile
});

const mapDispatchToProps = {};

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(Header);

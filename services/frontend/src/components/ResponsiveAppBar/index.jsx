import React, { useState, useEffect } from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import Menu from "@mui/material/Menu";
import MenuIcon from "@mui/icons-material/Menu";
import CastForEducationSharpIcon from "@mui/icons-material/CastForEducationSharp";
import Container from "@mui/material/Container";
import { red } from '@mui/material/colors';
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import Tooltip from "@mui/material/Tooltip";
import MenuItem from "@mui/material/MenuItem";
import { useHistory } from "react-router-dom";

import { connect } from "react-redux";
import { logoutAction } from "../LoginPage/actions";
import { redirect } from "statuses";
import { profile_fullname } from "../../helpers/profile";

const pages = ["Profile", "Dashboard"];
const settings = ["Profile", "Dashboard", "Logout"];

const ResponsiveAppBar = ({ profile, logoutAction }) => {
  const history = useHistory();
  const [anchorElNav, setAnchorElNav] = useState(null);
  const [anchorElUser, setAnchorElUser] = useState(null);

  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseNavMenu = (setting) => {
    switch (setting) {
      case "Profile":
        history.push("/");
        break;
      case "Dashboard":
        history.push("/dashboard");
        break;
      case "Logout":
        logoutAction(history);
        break;
    }
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <CastForEducationSharpIcon sx={{ mr: 2, fontSize: 40 }} />
          <Box sx={{ flexGrow: 1, display: { xs: "none", md: "flex" } }}>
            {pages.map((page) => (
              <Button
                key={page}
                onClick={() => handleCloseNavMenu(page)}
                sx={{ my: 2, color: "white", display: "block" }}
              >
                {page}
              </Button>
            ))}
          </Box>
          <Typography textAlign="center" sx={{ mr: 2 }}>
            {profile ? profile_fullname(profile) : ""}
          </Typography>
          <Box sx={{ flexGrow: 0 }}>
            <Tooltip title="Open settings">
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                <Avatar sx={{ bgcolor: red[400] }} aria-label="recipe">
                  {profile?.name ? profile.name[0] : 'Name'}
                </Avatar>
              </IconButton>
            </Tooltip>
            <Menu
              sx={{ mt: "45px" }}
              id="menu-appbar"
              anchorEl={anchorElUser}
              anchorOrigin={{
                vertical: "top",
                horizontal: "right",
              }}
              keepMounted
              transformOrigin={{
                vertical: "top",
                horizontal: "right",
              }}
              open={Boolean(anchorElUser)}
              onClose={handleCloseUserMenu}
            >
              {settings.map((setting) => (
                <MenuItem
                  key={setting}
                  onClick={() => handleCloseNavMenu(setting)}
                >
                  <Typography textAlign="center">{setting}</Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};

const mapStateToProps = (rootState) => ({
  profile: rootState?.profile,
});

const mapDispatchToProps = {
  logoutAction,
};

export default connect(mapStateToProps, mapDispatchToProps)(ResponsiveAppBar);

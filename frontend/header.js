import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  const DASHBOARD_URL = process.env.REACT_APP_DASHBOARD_URL;
  const PROFILE_URL = process.env.REACT_APP_PROFILE_URL;
  const ABOUT_URL = process.env.REACT_APP_ABOUT_URL;

  return (
    <header>
      <nav>
        <ul>
          <li><Link to={DASHBOARD_URL}>Dashboard</Link></li>
          <li><Link to={PROFILE_URL}>Profile</Link></li>
          <li><Link to={ABOUT_URL}>About Us</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
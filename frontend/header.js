import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  const DASHBOARD_URL = process.env.REACT_APP_DASHBOARD_URL;
  const PROFILE_URL = process.env.REACT_APP_PROFILE_URL;
  const ABOUT_URL = process.env.REACT_APP_ABOUT_URL;
  const [isNavVisible, setIsNavVisible] = useState(false);

  const toggleNav = () => {
    setIsNavVisible(prevState => !prevState);
  };

  return (
    <header>
      <nav>
        <button onClick={toggleNav} className="nav-toggle" aria-label="toggle navigation">
          Menu
        </button>
        <ul className={`nav-links ${isNavVisible ? 'show-nav' : ''}`}>
          <li><Link to={DASHBOARD_URL} onClick={() => setIsNavVisible(false)}>Dashboard</Link></li>
          <li><Link to={PROFILE_URL} onClick={() => setIsNavVisible(false)}>Profile</Link></li>
          <li><Link to={ABOUT_URL} onClick={() => setIsNavVisible(false)}>About Us</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
```

```css
.nav-toggle {
  display: none;
  background-color: #333;
  color: white;
  padding: 10px 20px;
  font-size: 20px;
  border: none;
  cursor: pointer;
}

.nav-links {
  list-style: none;
  overflow: hidden;
}

.nav-links li {
  padding: 15px 0;
}

.nav-links li a {
  text-decoration: none;
  color: #333;
}

@media screen and (max-width: 600px) {
  .nav-toggle {
    display: block;
  }

  .nav-links {
    display: none;
    flex-direction: column;
  }

  .nav-links.show-nav {
    display: flex;
  }
}
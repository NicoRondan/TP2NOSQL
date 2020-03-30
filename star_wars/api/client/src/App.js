import React, { Fragment } from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom';
//Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';

// Components 
import Navigation from './components/Navigation';
import EpisodeList from './components/EpisodeList';
import CreateCharacter from './components/CreateCharacter';

function App() {
  return (
    <Fragment>
      <Router>
        <Navigation/>
        <div className="container p-4">
          <Route exact path="/" component={EpisodeList} />
          <Route path="/create/:episode" component={CreateCharacter} />
        </div>
      </Router>
    </Fragment>
  );
}

export default App;

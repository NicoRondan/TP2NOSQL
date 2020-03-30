import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import {v4 as uuid} from 'uuid';

const EPISODES = [ "1", "2" ,"3", "4", "5", "6", "7", "8", "9"];

const EpisodeList = () => {
    const [episodes] = useState(EPISODES);

    return (
        <div className="row">
            {
                episodes.map(episode => (
                    <div className="col-md-4 p-2" key={uuid()}>
                        <div className="card">
                        <div className="card-header d-flex justify-content-between">
                            <h5>Episode {episode}</h5>
                            <Link to={`/create/${episode}`} className="btn btn-secondary">
                                See Characters
                            </Link>
                        </div>
                        </div>
                    </div>
                ))
            }
        </div>
    );
}

export default EpisodeList;

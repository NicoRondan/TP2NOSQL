import React, {useEffect, useState} from 'react'
import axios from 'axios';
import {v4 as uuid} from 'uuid';

export default function CreateCharacter(props) {
    const [characters, setCharacters] = useState([]);
    const [character, setCharacter] = useState('');
    const [episode] = useState(props.match.params.episode);

    useEffect(() => {
        getData(episode);
    }, [episode]);

    const getData = async (episode) => {
        const res = await axios.get(`http://localhost:4000/api/star-wars/${episode}`);
        setCharacters(res.data);
    };

    const onChangeCharacter = (e) => {
        setCharacter(e.target.value);
    };

    const onSubmit = async (e) => {
        e.preventDefault();
        const res = await axios.post(`http://localhost:4000/api/star-wars/${episode}/${character}`);
        console.log(res);
        setCharacter('');
        getData(episode);
    };

    const deleteCharacter = async (pj) => {
        await axios.delete(`http://localhost:4000/api/star-wars/${episode}/${pj}`);
        getData(episode);
    };

    return (
        <div className="row">
            <div className="col-md-4">
                <div className="card card-body">
                    <h3>Create New Character</h3>
                    <form onSubmit={onSubmit}>
                        <div className="form-group">
                            <input 
                            type="text"
                            value={character}
                            className="form-control"  
                            onChange={onChangeCharacter} 
                            required
                            />
                        </div>
                        <button type="submit" className="btn btn-secondary">
                            Save
                        </button>
                    </form> 
                </div>
            </div>
            {/*Doble clic para eliminar un personaje */}
            <div className="col-md-8">
                {(characters.length === 0) ? (
                    <div className="alert alert-dark  alert-dismissible fade show text-center" role="alert">
                        <strong>Characters Not Found</strong>
                        <button type="button" className="close" data-dismiss="alert" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                ) : (
                    <ul className="list-group">
                    {
                        characters.map(character => 
                        (<li 
                        key={uuid()} 
                        className="list-group-item list-group-item-action"
                        style={{cursor: 'pointer'}}
                        >
                            {character}
                            <button 
                            type="button" 
                            className="close" 
                            aria-label="Close"
                            onClick={() => deleteCharacter(character)}>
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </li>))
                    }
                </ul>
                )}
            </div>
        </div>
    )
}
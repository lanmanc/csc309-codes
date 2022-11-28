import {createContext, useState} from "react";

export const useAPIContext = () => {
    const [players, setPlayers] = useState([]);

    return {
        players,
        setPlayers,
    }
}

const APIContext = createContext({
    players: null, setPlayers: () => {},
})

export default APIContext;
import {useEffect, useState} from "react";

const Players = () => {
    const perPage = 25;
    const [players, setPlayers] = useState([]);

    const [query, setQuery] = useState({page: 1, search: ''})

    useEffect(() => {
        const { page, search } = query;
        fetch(`https://www.balldontlie.io/api/v1/players?page=${page}&per_page=${perPage}&search=${search}`)
            .then(res => res.json())
            .then(json => {
                setPlayers(json.data);
            })
    }, [query])

    return (
        <>
            Search
            <input
                style={{width: 200, height: 30, fontSize: 18, margin: 4}}
                value={query.search}
                onChange={(event) => {
                    setQuery({
                        search: event.target.value,
                        page: 1,
                    })
                }}
            />
            <table>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>First name</th>
                        <th>Last name</th>
                        <th>Height</th>
                        <th>Position</th>
                        <th>Team</th>
                    </tr>
                </thead>
                <tbody>
                {players.map((player, index) => (
                    <tr key={player.id}>
                        <td>{ (query.page - 1) * perPage + index + 1 }</td>
                        <td>{ player.first_name }</td>
                        <td>{ player.last_name }</td>
                        <td>{ player.height_feet ? `${player.height_feet}' ${player.height_inches}"` : ''}</td>
                        <td>{ player.position }</td>
                        <td>{ player.team.name }</td>
                    </tr>
                ))}
                </tbody>
            </table>
            <button onClick={() => setQuery({
                ...query,
                page: Math.max(1, query.page - 1)
            })}>prev</button>
            <button onClick={() => setQuery({
                ...query,
                page: query.page + 1
            })}>next</button>
        </>
    )
}

export default Players;
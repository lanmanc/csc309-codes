import {useContext, useEffect, useState} from "react";
import PlayersTable from "./PlayersTable";
import {APIContext} from "../../Contexts/APIContext";

const Players = () => {
    const perPage = 20;
    const [params, setParams] = useState({page: 1, search: ""})

    const { setPlayers } = useContext(APIContext);

    useEffect(() => {
        const { page, search } = params;
        fetch(`https://www.balldontlie.io/api/v1/players?page=${page}&per_page=${perPage}&search=${search}`)
            .then(res => res.json())
            .then(json => {
                setPlayers(json.data);
            })
    }, [params])

    return (
        <>
            Search
            <input
                style={{width: 300, height: 20, fontSize: 18, margin: 4}}
                value={params.search}
                onChange={(event) => {
                    setParams({
                        search: event.target.value,
                        page: 1,
                    })
                }}
            />
            <PlayersTable perPage={perPage} params={params} />
            <button onClick={() => setParams({
                ...params,
                page: Math.max(1, params.page - 1)
            })}>
                prev
            </button>
            <button onClick={() => setParams({
                ...params,
                page: params.page + 1
            })}>
                next
            </button>
        </>
    )
}

export default Players;
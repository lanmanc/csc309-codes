import {useContext} from "react";
import {APIContext} from "../../../Contexts/APIContext";

const PlayersTable = ({ perPage, params }) => {
    const { players } = useContext(APIContext);

    return <table>
        <thead>
        <tr>
            <th> # </th>
            <th> First name </th>
            <th> Last name </th>
            <th> Height </th>
            <th> Position </th>
            <th> Team </th>
        </tr>
        </thead>
        <tbody>
        {players.map((player, index) => (
            <tr key={player.id}>
                <td>{ (params.page - 1) * perPage + index + 1 }</td>
                <td>{ player.first_name }</td>
                <td>{ player.last_name }</td>
                <td>
                    { player.height_feet ? `${player.height_feet}' ${player.height_inches}"`: ''}
                </td>
                <td>{ player.position }</td>
                <td>{ player.team.name }</td>
            </tr>
        ))}
        </tbody>
    </table>
}

export default PlayersTable;
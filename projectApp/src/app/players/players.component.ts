/* Imports */

import { Component } from '@angular/core';
import { WebService } from '../web.service';

@Component({
  selector: 'players',
  templateUrl: './players.component.html',
  styleUrls: ['./players.component.css']
})

/* Player Componentnand constructor to affect what info is shown about a player using Auth0 */
export class PlayersComponent {

  players_list: any = [];
  page: number = 1;
  public playerName: any = "";

  constructor(public webService: WebService) { }

  ngOnInit(){
    /* Storage of what the current page is */
    if (sessionStorage['page']){
      this.page = Number (sessionStorage['page'])
    }
    this.players_list = this.webService.getPlayers(this.page);
  }

  /* Previous Page Function */
  previousPage() {
    if (this.page > 1) {
      this.page = this.page - 1;
      sessionStorage['page'] = this.page;
      this.players_list = this.webService.getPlayers(this.page);
    }

  }
  /* Next Page Function  */
  nextPage() {
    this.page = this.page + 1;
    sessionStorage['page'] = this.page;
    this.players_list = this.webService.getPlayers(this.page);
  }


  /* Create New Player Function */
  createNewPlayer(){
    const playerData = {
      playerName: this.playerName
    }
console.log("create called");

    this.webService.postPlayer(playerData);
  }


  /* Delete Player Function */
  deletePlayer(playerId: string){
    this.webService.deletePlayer(playerId);
    location.reload();
  }
}


import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  
  

  constructor(private http: HttpClient) { }

  GetPlayer() {
    return this.http.get('http://localhost:5000/api/v1.0/players?ps=1000000');
  }

  GetPlayerByName(name: any) {
    console.log("Search for:", name);
    
    return this.http.get(`http://localhost:5000/api/v1.0/players/name/${name}`);
  }

  Delete(id:any) {
    return this.http.delete(`http://localhost:5000/api/v1.0/players/${id}`);
  }

  GetOnePlayer(id: any) {
    return this.http.get(`http://localhost:5000/api/v1.0/players/${id}`);
  }

  SavePlayer(player: any) {

    var formData = new FormData();
    
    for (var key in player) {
        formData.append(key, player[key]);
    }

    return this.http.put(`http://localhost:5000/api/v1.0/players/${player._id}`, formData);
  }

  AddPlayer(player: any) {
    var formData = new FormData();
    
    for (var key in player) {
        formData.append(key, player[key]);
    }

    console.log(player);
    

    return this.http.post(`http://localhost:5000/api/v1.0/players`, player);
  }
}

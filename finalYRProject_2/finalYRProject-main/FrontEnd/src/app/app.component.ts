import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit {
  public title = 'FrontEnd';

  public items: MenuItem[] | undefined;

  ngOnInit() {
      this.items = [
          {
              label: 'Players',
              icon: 'pi pi-fw pi-file',
              routerLink: 'home',
          },
          {
            label: 'Add Player',
            icon: 'pi pi-fw pi-file',
            routerLink: 'add',
          },
          {
            label: 'Login',
            icon: 'pi pi-fw pi-file',
            routerLink: 'login',
        },
        ];
  }
}

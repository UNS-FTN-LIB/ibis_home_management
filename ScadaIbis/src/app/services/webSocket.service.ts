import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';

@Injectable({
  providedIn: 'root'
})
export class WebSocketService {
  private socket$: WebSocketSubject<any>;

  constructor() {
    // Povezivanje sa WebSocket serverom
    this.socket$ = webSocket('ws://localhost:8765'); // Zamijenite sa vašim WebSocket URL-om
  }

  sendMessage(message: string) {
    // Slanje poruke serveru
    this.socket$.next(message);
  }

  getMessage(): Observable<any> {
    // Prijem poruka od servera
    return this.socket$;
  }
}

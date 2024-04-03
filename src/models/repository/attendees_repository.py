from src.models.settings.connection import db_connection_handler
from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import NoResultFound
from typing import Dict

class AttendeesRepository:
        
    def insert_attendee(self, attendde_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                Attendee = (
                      Attendees(
                          id = attendde_info.get("uuid"),
                          name = attendde_info.get("name"),
                          email = attendde_info.get("email"),
                          event_id = attendde_info.get("event_id")
                      )
                  )
                
                database.session.add(Attendee)
                database.session.commit()
                
                return attendde_info
            
            except IntegrityError:
                raise Exception("Participante já cadastrado!")
            
            except Exception as exception:
               database.session.rollback()
               raise exception
    
    def get_attendee_badge_by_id(Self, attendee_id: str):
        with db_connection_handler as database:
            try:
                attendee = (
                    database.session
                        .query(Attendees)
                        .join(Events, Events.id == Attendees.event_id)
                        .filter(Attendees.id == attendee_id)
                        .with_entities(
                            Attendees.name,
                            Attendees.email,
                            Events.title
                            
                        )
                        .one()
                )
                return attendee
            except NoResultFound:
                return None
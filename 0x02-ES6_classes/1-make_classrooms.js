import ClassRoom from './0-classroom';

/**
 * Creaing array
 * @return v
 */
export default function initializeRooms() {
  return [19, 20, 34].map((size) => new ClassRoom(size));
}

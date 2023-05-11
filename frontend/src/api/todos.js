import { client } from "./client.js";

/**
 * API abstraction for the "Todo" model on the backend.
 */
export const todos = {
  /**
   * Returns the backend route (route only, not full URL) of the "Todo"
   * resource.
   * 
   * @param {number} id Todo ID 
   */
  route(id = null) {
    return id ? `/todos/${id}` : "/todos/";
  },

  /**
   * Returns the full URL of the "Todo" resource on the backend.
   * 
   * @param {number} id Todo ID 
   */
  url(id = null) {
    return client.getUri({ url: this.route(id) });
  },

  /**
   * Makes an HTTP GET request to obtain all the todos or a single todo.
   * 
   * @param {number} id 
   */
  get(id = null) {
    return client.get(this.route(id));
  },

  /**
   * Makes an HTTP POST request to create a todo.
   * 
   * @param {number} id 
   */
  post(data) {
    return client.post(this.route(), data);
  },

  /**
   * Makes an HTTP PUT request to modify todo.
   * 
   * @param {number} id 
   */
  put(id, data) {
    return client.put(this.route(id), data);
  },

  /**
   * Makes an HTTP DELETE request to remove a todo.
   * 
   * @param {number} id 
   */
  delete(id) {
    return client.delete(this.route(id));
  }
}

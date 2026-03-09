import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
//for validating inputs using Zod
import { z } from "zod";

// 1. Create server
const server = new McpServer({
  name: "first-mcp-server",
  version: "1.0.0",
  capabilities: {
    tools: {},
  },
});

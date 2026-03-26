from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# TODO: Write a tool to read a doc
@mcp.tool(
    name = 'read_doc',
    description = 'Read the contents of a document.',
)
def read_doc(doc_id: str = Field(description="The ID of the document to read")):
    if doc_id in docs:
        return docs[doc_id]
    else:        
        return "Document not found."
# TODO: Write a tool to edit a doc
@mcp.tool(
    name = 'edit_doc',
    description = 'Edit the contents of a document.',
)
def edit_doc(doc_id: str = Field(description="The ID of the document to edit"), new_content: str = Field(description="The new content for the document"), old_content: str = Field(description="The old content of the document")):
    if doc_id in docs:
        if docs[doc_id] == old_content:
            docs[doc_id] = new_content
            return "Document updated successfully."
        else:
            return "Old content does not match."
    else:
        return "Document not found."

# TODO: Write a resource to return all doc id's
@mcp.resource(
    "docs://documents",
    mime_type="application/json",
)
def list_docs()->list[str]:
    return list(docs.keys())

# TODO: Write a resource to return the contents of a particular doc
@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain",
)
def fetch_doc(doc_id: str)->str:
    if doc_id in docs:
        return docs[doc_id]
    else:
        return "Document not found."
    
  # TODO: Write a prompt to rewrite a doc in markdown format
@mcp.prompt(
    "rewrite_doc",
    description="Rewrite a doc in markdown format.",
)
def rewrite_doc(doc_id: str)->str:
    if doc_id in docs:
        return docs[doc_id]
    else:
        return "Document not found."

# TODO: Write a prompt to summarize a doc
@mcp.prompt(
    "summarize_doc",
    description="Summarize a doc.",
)
def summarize_doc(doc_id: str)->str:
    if doc_id in docs:
        return docs[doc_id]
    else:
        return "Document not found."

if __name__ == "__main__":
    mcp.run(transport="stdio")

import { Router, Request, Response } from "express";

const router = Router();

router.get("/", async (request: Request, response: Response) => {
    return response.send("index.html");
});

export default router;